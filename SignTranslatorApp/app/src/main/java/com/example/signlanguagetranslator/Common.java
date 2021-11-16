package com.example.signlanguagetranslator;


import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class Common {
    public static Retrofit retrofit =null;
    public static String url="http://192.168.1.106:5000/";
    public static Retrofit getClient(){
        if(retrofit==null)
        {
            retrofit=new Retrofit.Builder()
                    .baseUrl(Common.url)
                    .addConverterFactory(GsonConverterFactory.create()) //Here we are using the GsonConverterFactory to directly convert json data to object
                    .build();

        }
        return retrofit;
    }
    public static networkInterface getApiService(){
        return retrofit.create(networkInterface.class);
    }

}
