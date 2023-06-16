package com.example.ero;
public class Attendance {
    private String name;
    private String status;
    private String dateTime;
    private String usn;
    private String subject; // New field

    public Attendance() {
    }

    public Attendance(String name, String status, String dateTime, String subject) {
        this.name = name;
        this.status = status;
        this.dateTime = dateTime;
        this.usn = usn;
        this.subject = subject; // Initialize new field
    }

    public String getName() {
        return name;
    }

    public String getStatus() {
        return status;
    }

    public String getDateTime() {
        return dateTime;
    }
    public String getUSN() {
        return usn;
    }

    public String getSubject() {
        return subject; // Getter for new field
    }
}
