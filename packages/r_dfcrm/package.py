# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfcrm(RPackage):
	"""Dose-Finding by the Continual Reassessment Method

	Provides functions to run the CRM and
        TITE-CRM in phase I trials and calibration tools for trial
        planning purposes.
	"""
	
	homepage = "http://www.columbia.edu/~yc632"
	cran = "dfcrm" 

	version("0.2-2.1", md5="2fb6fd740797583e3ae8c4ef5f1c98dd")

