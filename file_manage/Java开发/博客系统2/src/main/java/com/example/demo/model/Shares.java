package com.example.demo.model;

import javax.persistence.*;

@Entity
public class Shares {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "shareid")
    private int shareId;
    private int userId;
    private int postId;
    public int getShareId() {
        return shareId;
    }
    public void setShareId(int shareId) {
        this.shareId = shareId;
    }
    public int getUserId() {
        return userId;
    }
    public void setUserId(int userId) {
        this.userId = userId;
    }
    public int getPostId() {
        return postId;
    }
    public void setPostId(int postId) {
        this.postId = postId;
    }
}
