package com.example.ero;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;


public class home extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);

        // Get the Intent that started this activity
        Intent intent = getIntent();
        String subject = "maths";
        // Extract the name value from the Intent
        String name = intent.getStringExtra("Name");

        // Now, you can use 'name' in your activity
        // For example, let's display the name in a TextView
        TextView nameTextView = findViewById(R.id.name_text_view);
        String greet = "HI "+name+"!!";
        nameTextView.setText(greet);
        Button startButton = findViewById(R.id.button);
        startButton.setOnClickListener(v -> {
            Intent intent1 = new Intent(home.this, MainActivity.class);
            intent1.putExtra("Subject", subject);
            startActivity(intent1);
        });
        Button startButton2 = findViewById(R.id.button2);
        startButton2.setOnClickListener(v1 -> {
            Intent intent4 = new Intent(home.this, specific_attend.class);

            intent4.putExtra("Name", name);
            startActivity(intent4);
        });
        Button startButton3 = findViewById(R.id.button3);
        startButton3.setOnClickListener(v1 -> {
            Intent intent5 = new Intent(home.this, imagedisp.class);
            intent5.putExtra("Name", name);
            startActivity(intent5);
        });
    }
}