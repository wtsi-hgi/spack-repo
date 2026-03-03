# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMonitor(RPackage):
	"""Acoustic Template Detection in R

	Acoustic template detection and monitoring database interface. Create, modify, save, and use templates for detection of animal vocalizations. View, verify, and extract results. Upload a MySQL schema to a existing instance, manage survey metadata, write and read templates and detections locally or to the database. 
	"""
	
	homepage = "http://www.uvm.edu/rsenr/vtcfwru/R/?Page=monitoR/monitoR.htm"
	cran = "monitoR" 

	version("1.0.7", md5="7b782b6d1e6ea93ca2c8b26e25aa9d64")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
