# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdaptr(RPackage):
	"""Adaptive Trial Simulator

	Package that simulates adaptive (multi-arm, multi-stage) clinical
    trials using adaptive stopping, adaptive arm dropping, and/or adaptive
    randomisation. Developed as part of the INCEPT (Intensive Care Platform
    Trial) project (<https://incept.dk/>), which is primarily supported by a
    grant from Sygeforsikringen "danmark" (<https://www.sygeforsikring.dk/>).
	"""
	
	homepage = "https://inceptdk.github.io/adaptr/"
	cran = "adaptr" 

	version("1.3.2", md5="a111de088784083aa27e2eb59ea4376c")

