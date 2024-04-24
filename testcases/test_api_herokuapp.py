import pytest
import requests
import allure

@pytest.mark.usefixtures("post_booking_details","auth_token","read_config_api","api_data")
class TestAPIHerokuApp :

    @pytest.mark.run(order=5)
    def test_get_all_bookingDetails(self,read_config_api,auth_token) :
        api_config = read_config_api
        response = requests.get(api_config["api_url"] + api_config["booking_base_endpoint"],
                                headers= {"Cookie" : "token="+auth_token})
        assert response.status_code == 200 , f"Failed to get all booking Ids Status code : {response.status_code}"
        data = response.json()
        assert any("bookingid" in item for item in data) , "No booking details found"
      

    @pytest.mark.run(order=6)
    def test_create_booking(self,read_config_api,auth_token,api_data) :
        api_config = read_config_api
        response = requests.post(api_config["api_url"] + api_config["booking_base_endpoint"],
                                 json = api_data.get("bookingdetails", {}), headers= { 'Cookie' : 'token=' + auth_token})
        assert response.status_code == 200 , f"Failed to create booking. Status  code : {response.status_code}"
        data = response.json()
        assert data.get("bookingid", '') != '' , "No booking Id found"
        print(data)

    @pytest.mark.run(order=7)
    def test_get_bookingById(self,read_config_api,auth_token,post_booking_details) :
        api_config = read_config_api
        response = requests.get(api_config["api_url"] + api_config["bookind_detail_endpoint"].format(bookingid = post_booking_details))
        assert response.status_code == 200 , f"Failed to get booking details. Status code : {response.status_code}"
        data = response.json()
        print(data)

    @pytest.mark.run(order=8)
    def test_update_bookingdetails(self,read_config_api,auth_token,api_data,post_booking_details) :
        api_config = read_config_api
        response = requests.put(api_config["api_url"] + api_config["bookind_detail_endpoint"].format(bookingid = post_booking_details),
                                json = api_data.get("update_booking_details", {}), headers= { 'Cookie' : 'token=' + auth_token})
        assert response.status_code == 200 , f"Failed to update booking. Status  code : {response.status_code}"
        data = response.json()
        print("Updated booking details")
        print(data)


    @pytest.mark.run(order=9)
    def test_patch_bookingdetails(self,read_config_api,auth_token,api_data,post_booking_details) :
        api_config = read_config_api
        response = requests.patch(api_config["api_url"] + api_config["bookind_detail_endpoint"].format(bookingid = post_booking_details),
                                  json= api_data.get("patch_data" , {}) , headers= { 'Cookie' : 'token=' + auth_token})
        assert response.status_code == 200 , f"Failed to patch booking. Status  code : {response.status_code}"
        data = response.json()
        print("Patched booking details")
        print(data)

    @pytest.mark.run(order=10)
    def test_delete_bookingdetails(self,read_config_api,auth_token,post_booking_details) :
        api_config = read_config_api
        response = requests.delete(api_config["api_url"] + api_config["bookind_detail_endpoint"].format(bookingid = post_booking_details) ,
                                   headers = { 'Cookie' : 'token=' + auth_token})
        assert response.status_code == 201 , f"Failed to delete booking. Status  code : {response.status_code}"
