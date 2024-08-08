from sqlalchemy import Column, String, Integer, BigInteger, Enum, DateTime, ForeignKey, Float, Boolean, Text, func
from sqlalchemy.orm import relationship, Session
from datetime import datetime
from app.database import Base

class BaseEntity:
    create_date = Column(DateTime, default=datetime.utcnow)
    update_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Comment(Base, BaseEntity):
    __tablename__ = 'comment'
    comment_id = Column(BigInteger, primary_key=True, index=True)
    content = Column(String(255))
    member_id = Column(Integer, ForeignKey('member.member_id'))
    review_id = Column(BigInteger, ForeignKey('review.review_id'))

    member = relationship("Member", back_populates="comments")
    review = relationship("Review", back_populates="comments")

class Empathy(Base):
    __tablename__ = 'empathy'
    member_member_id = Column(Integer, ForeignKey('member.member_id'), primary_key=True)
    review_review_id = Column(BigInteger, ForeignKey('review.review_id'), primary_key=True)

    member = relationship("Member", back_populates="empathies")
    review = relationship("Review", back_populates="empathies")

class Member(Base, BaseEntity):
    __tablename__ = 'member'
    member_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(255), unique=True, index=True)
    nickname = Column(String(255), unique=True)
    profile = Column(String(255))
    type = Column(Enum('ADMIN', 'USER'))

    comments = relationship("Comment", back_populates="member")
    schedules = relationship("Schedule", back_populates="member")
    reservations = relationship("Reservation", back_populates="member")
    empathies = relationship("Empathy", back_populates="member")
    categories = relationship("MemberCategories", back_populates="member")

class MemberCategories(Base):
    __tablename__ = 'member_categories'
    member_member_id = Column(Integer, ForeignKey('member.member_id'), primary_key=True)
    categories = Column(Enum('PLAY', 'MOVIE', 'PERFORMANCE', 'CONCERT', 'MUSICAL', 'EXHIBITION', 'ETC'))

    member = relationship("Member", back_populates="categories")

class PriceBySeatClass(Base):
    __tablename__ = 'price_by_seat_class'
    show_detail_id = Column(BigInteger, ForeignKey('show_detail.show_detail_id'), primary_key=True)
    price_by_seat_class = Column(Integer, primary_key=True)
    price_by_seat_class_price = Column(String(255))

    show_detail = relationship("ShowDetail", back_populates="price_by_seat_classes")

class Reservation(Base, BaseEntity):
    __tablename__ = 'reservation'
    reserve_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    reserve_amount = Column(String(255))
    reserve_comment = Column(String(255))
    reserve_date = Column(DateTime)
    is_refunded = Column(Boolean)
    member_id = Column(Integer, ForeignKey('member.member_id'))

    member = relationship("Member", back_populates="reservations")
    details = relationship("ReservationDetail", back_populates="reservation")

class ReservationDetail(Base):
    __tablename__ = 'reservation_detail'
    reserve_detail_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    seat_col = Column(Integer)
    seat_row = Column(Integer)
    reserve_id = Column(BigInteger, ForeignKey('reservation.reserve_id'))
    show_schedule_id = Column(BigInteger, ForeignKey('show_schedule.show_schedule_id'))

    reservation = relationship("Reservation", back_populates="details")
    schedule = relationship("ShowSchedule", back_populates="details")

class Review(Base, BaseEntity):
    __tablename__ = 'review'
    review_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    review_content = Column(String(255))
    review_emotion = Column(Integer)
    # empathy_number = Column(Integer)
    review_filename = Column(String(255))
    is_spoiler = Column(Boolean)
    schedule_id = Column(BigInteger, ForeignKey('schedule.schedule_id'))

    comments = relationship("Comment", back_populates="review")
    empathies = relationship("Empathy", back_populates="review")
    schedule = relationship("Schedule", back_populates="reviews")

class Schedule(Base):
    __tablename__ = 'schedule'
    dtype = Column(String(31))
    schedule_id = Column(BigInteger, primary_key=True, index=True)
    schedule_image = Column(String(255))
    schedule_category = Column(Enum('PLAY', 'MOVIE', 'PERFORMANCE', 'CONCERT', 'MUSICAL', 'EXHIBITION', 'ETC'))
    # enum 느낌으로 공연에 대한 영역
    schedule_date_time = Column(DateTime)
    schedule_latitude = Column(Float)
    schedule_longitude = Column(Float)
    schedule_location = Column(String(255))
    schedule_name = Column(String(255))
    schedule_seat = Column(String(255))
    member_id = Column(Integer, ForeignKey('member.member_id'))
    reserve_detail_id = Column(BigInteger, ForeignKey('reservation_detail.reserve_detail_id'))

    member = relationship("Member", back_populates="schedules")
    reviews = relationship("Review", back_populates="schedule")

class Seat(Base):
    __tablename__ = 'seat'
    seat_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    seat_col = Column(Integer)
    seat_row = Column(Integer)
    seat_class = Column(String(255))
    show_detail_id = Column(BigInteger, ForeignKey('show_detail.show_detail_id'))

    show_detail = relationship("ShowDetail", back_populates="seats")

class ShowDetail(Base):
    __tablename__ = 'show_detail'
    show_detail_id = Column(BigInteger, primary_key=True, index=True)
    show_detail_api_id = Column(String(255))
    show_detail_area = Column(String(255))
    show_detail_cast = Column(String(255))
    show_detail_category = Column(Enum('PLAY', 'MOVIE', 'PERFORMANCE', 'CONCERT', 'MUSICAL', 'EXHIBITION', 'ETC'))
    show_hall = Column(String(255))
    show_detail_name = Column(String(255))
    show_detail_poster_image_path = Column(String(255))
    show_detail_runtime = Column(String(255))
    show_detail_state = Column(Enum('COMPLETED', 'SCHEDULED', 'SHOWING'))
    theater_id = Column(BigInteger, ForeignKey('theater.theater_id'))

    price_by_seat_classes = relationship("PriceBySeatClass", back_populates="show_detail")
    schedules = relationship("ShowSchedule", back_populates="show_detail")
    seats = relationship("Seat", back_populates="show_detail")
    theater = relationship("Theater", back_populates="show_details")

class ShowSchedule(Base):
    __tablename__ = 'show_schedule'
    show_schedule_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    show_schedule_date_time = Column(DateTime)
    show_detail_id = Column(BigInteger, ForeignKey('show_detail.show_detail_id'))

    show_detail = relationship("ShowDetail", back_populates="schedules")
    details = relationship("ReservationDetail", back_populates="schedule")

class Theater(Base):
    __tablename__ = 'theater'
    theater_id = Column(BigInteger, primary_key=True, index=True)
    theater_address = Column(String(255))
    theater_api_id = Column(String(255))
    theater_latitude = Column(Float)
    theater_longitude = Column(Float)
    theater_name = Column(String(255))

    show_details = relationship("ShowDetail", back_populates="theater")
