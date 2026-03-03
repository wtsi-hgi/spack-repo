# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJalcal(RPackage):
	"""Conversion Between Jalali (Persian or Solar Hijri) and Gregorian
Calendar Dates

	Jalali, also known as Persian, Solar Hijri and Hijri Shamsi calendar is 
    the official calendar of Iran and Afghanistan. It begins on Nowruz, the March equinox, 
    as determined by astronomical calculation and has years of 365 or 366 days. 
    Adapting the algorithms in <https://jdf.scr.ir/>, this package provides tools 
    for converting the Jalali and Gregorian dates.
	"""
	
	homepage = "https://github.com/jalilian/jalcal"
	cran = "jalcal" 

	version("0.1.0", md5="21e348ac894c2e1bc90c20c23bfa93c8")

