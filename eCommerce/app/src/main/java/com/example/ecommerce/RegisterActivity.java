package com.example.ecommerce;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;

public class RegisterActivity extends AppCompatActivity {

    private Button CreateAccoutbutton;
    private EditText InputName,InputPhonenumber,InputPassword;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        CreateAccoutbutton = (Button) findViewById(R. id. register_btn);
        InputName = (EditText) findViewById(R. id. register_username_input);
        InputPhonenumber = (EditText) findViewById(R. id. register_phone_number_input);
        InputPassword = (EditText) findViewById(R. id. register_password_input);
    }
}
