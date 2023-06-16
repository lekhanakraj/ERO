package com.example.ero;

import static android.content.ContentValues.TAG;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.auth.UserProfileChangeRequest;

public class Authentication extends AppCompatActivity {
    private FirebaseAuth mAuth;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_authentication);

        mAuth = FirebaseAuth.getInstance();
        EditText nameEditText = findViewById(R.id.name);
        EditText universityNumberEditText = findViewById(R.id.university_number);
        EditText passwordEditText = findViewById(R.id.password);
        Button registerButton = findViewById(R.id.register);
        registerButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String name = nameEditText.getText().toString();
                String universityNumber = universityNumberEditText.getText().toString();
                String password = passwordEditText.getText().toString();

                registerUser(name, universityNumber, password);
            }
        });
    }

    private void registerUser(String name, String universityNumber, String password) {
        mAuth.createUserWithEmailAndPassword(universityNumber+"@gmail.com", password)
                .addOnCompleteListener(new OnCompleteListener<AuthResult>() {
                    @Override
                    public void onComplete(@NonNull Task<AuthResult> task) {
                        if (task.isSuccessful()) {
                            // Sign up success, update UI with the signed-in user's information
                            FirebaseUser user = mAuth.getCurrentUser();
                            UserProfileChangeRequest profileUpdates = new UserProfileChangeRequest.Builder()
                                    .setDisplayName(name).build();

                            user.updateProfile(profileUpdates)
                                    .addOnCompleteListener(new OnCompleteListener<Void>() {
                                        @Override
                                        public void onComplete(@NonNull Task<Void> task) {
                                            if (task.isSuccessful()) {
                                                Log.d(TAG, "User profile updated.");
                                                Intent intent = new Intent(Authentication.this, home.class);
                                                intent.putExtra("Name", name);
                                                startActivity(intent);
                                            }
                                        }
                                    });
                        } else {
                            // If sign up fails, display a message to the user.x`
                            Log.w(TAG, "createUserWithEmail:failure", task.getException());
                            Toast.makeText(Authentication.this, "Authentication failed.",
                                    Toast.LENGTH_SHORT).show();
                        }
                    }
                });
    }
}
