# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhawkes(RPackage):
	"""Renewal Hawkes Process

	The renewal Hawkes (RHawkes) process (Wheatley,
    Filimonov, and Sornette, 2016 <doi:10.1016/j.csda.2015.08.007>) is
    an extension to the classical Hawkes self-exciting point process
    widely used in the modelling of clustered event sequence data.
    This package provides functions to simulate the RHawkes process
    with a given immigrant hazard rate function and offspring birth
    time density function, to compute the exact likelihood of a
    RHawkes process using the recursive algorithm proposed by Chen and
    Stindl (2018) <doi:10.1080/10618600.2017.1341324>, to compute the
    Rosenblatt residuals for goodness-of-fit assessment, and to
    predict future event times based on observed event times up to a
    given time. A function implementing the linear time RHawkes
    process likelihood approximation algorithm proposed in Stindl and
    Chen (2021) <doi:10.1007/s11222-021-10002-0> is also included.
	"""
	
	cran = "RHawkes" 

	version("1.0", md5="e22590e2d36720e4faf02ee8a83dd854")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ihsep", type=("build", "run"))
