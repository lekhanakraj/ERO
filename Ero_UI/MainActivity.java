package com.example.ero;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import com.example.ero.Attendance;
public class MainActivity extends AppCompatActivity {
    private static final String TAG = "MainActivity";
    private TextView attendanceInfoTextView;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Intent intent = getIntent();

        // Extract the name value from the Intent
        String subject = intent.getStringExtra("Subject");
        attendanceInfoTextView = findViewById(R.id.textView);

        DatabaseReference mDatabase = FirebaseDatabase.getInstance().getReference();

        mDatabase.child("attendance").addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                attendanceInfoTextView.append(subject.toUpperCase()+"\n\n");
                for (DataSnapshot attendanceSnapshot: dataSnapshot.getChildren()) {
                    Attendance attendance = attendanceSnapshot.getValue(Attendance.class);
                    if (attendance.getSubject().toLowerCase().equals(subject)) {
                        attendanceInfoTextView.append(attendance.getName() + " " + attendance.getStatus() + "  " + attendance.getSubject() + "\n");
                    }                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError databaseError) {
                Log.w(TAG, "loadAttendance:onCancelled", databaseError.toException());
            }
        });
    }
}
