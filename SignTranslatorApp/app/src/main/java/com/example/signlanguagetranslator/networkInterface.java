package com.example.signlanguagetranslator;

import com.google.gson.JsonObject;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Query;

public interface networkInterface {
    @GET("/solve")
    Call<JsonObject> solve(
            @Query("image")String method
    );
}
