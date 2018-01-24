#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/thumbor/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com thumbor@googlegroups.com
'''
Thumbor engine. This class triggers events that should be implemented by each engine.

All methods are static coroutines.
'''

from tornado import gen

from thumbor.lifecycle import Events


class Engine(object):
    'Engine class. Triggers events captured by the engine blueprints.'

    @classmethod
    @gen.coroutine
    def read_image(cls, sender, details, buffer):
        '''
        Triggers the read image event.
        '''
        yield Events.trigger(
            Events.Engine.before_read_image,
            sender,
            details=details,
            buffer=buffer,
        )

        yield Events.trigger(
            Events.Engine.read_image,
            sender,
            details=details,
            buffer=buffer,
        )

        yield Events.trigger(
            Events.Engine.after_read_image,
            sender,
            details=details,
            buffer=buffer,
        )

    @classmethod
    @gen.coroutine
    def resize(cls, sender, details, width=0, height=0):
        '''
        Triggers the resize event.
        '''
        yield Events.trigger(
            Events.Engine.before_resize,
            sender,
            details=details,
            width=width,
            height=height,
        )

        yield Events.trigger(
            Events.Engine.resize,
            sender,
            details=details,
            width=width,
            height=height,
        )

        yield Events.trigger(
            Events.Engine.after_resize,
            sender,
            details=details,
            width=width,
            height=height,
        )

    @classmethod
    @gen.coroutine
    def crop(cls, sender, details, left, top, right, bottom):  # pylint: disable=too-many-arguments
        '''
        Triggers the crop image event.
        '''
        yield Events.trigger(
            Events.Engine.before_crop,
            sender,
            details=details,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
        )

        yield Events.trigger(
            Events.Engine.crop,
            sender,
            details=details,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
        )

        yield Events.trigger(
            Events.Engine.after_crop,
            sender,
            details=details,
            left=left,
            top=top,
            right=right,
            bottom=bottom,
        )

    @classmethod
    @gen.coroutine
    def reorientate(cls, sender, details):
        'Reorientates the image according to metadata'
        yield Events.trigger(
            Events.Engine.before_reorientate,
            sender,
            details=details,
        )

        yield Events.trigger(
            Events.Engine.reorientate,
            sender,
            details=details,
        )

        yield Events.trigger(
            Events.Engine.after_reorientate,
            sender,
            details=details,
        )

    @classmethod
    @gen.coroutine
    def get_image_data_as_rgb(cls, sender, details):
        'Get Image data as RGB Buffer'
        image_data = yield Events.trigger(
            Events.Engine.get_image_data_as_rgb,
            sender,
            details=details,
        )

        return image_data

    @classmethod
    @gen.coroutine
    def get_image_size(cls, sender, details):
        'Get Image size'
        image_size = yield Events.trigger(
            Events.Engine.get_image_size,
            sender,
            details=details,
        )
        return image_size

    @classmethod
    @gen.coroutine
    def serialize(cls, sender, details):
        '''
        Triggers the serialize image event.
        '''
        yield Events.trigger(
            Events.Engine.before_serialize,
            sender,
            details=details,
        )

        yield Events.trigger(
            Events.Engine.serialize,
            sender,
            details=details,
        )

        yield Events.trigger(
            Events.Engine.after_serialize,
            sender,
            details=details,
        )

    @classmethod
    @gen.coroutine
    def get_proportional_width(cls, sender, details, new_height):
        width, height = yield cls.get_image_size(sender, details)
        return round(float(new_height) * width / height, 0)

    @classmethod
    @gen.coroutine
    def get_proportional_height(cls, sender, details, new_width):
        width, height = yield cls.get_image_size(sender, details)
        return round(float(new_width) * height / width, 0)

    @classmethod
    @gen.coroutine
    def focus(cls, sender, details):
        yield Events.trigger(
            Events.Engine.before_focal_points_changed,
            sender,
            details=details,
            focal_points=details.focal_points,
        )

        yield Events.trigger(
            Events.Engine.focal_points_changed,
            sender,
            details=details,
            focal_points=details.focal_points,
        )

        yield Events.trigger(
            Events.Engine.after_focal_points_changed,
            sender,
            details=details,
            focal_points=details.focal_points,
        )