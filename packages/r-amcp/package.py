# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmcp(RPackage):
	"""A Model Comparison Perspective

	Accompanies "Designing experiments and 
    analyzing data: A model comparison perspective" (3rd ed.) by 
    Maxwell, Delaney, & Kelley (2018; Routledge). 
    Contains all of the data sets in the book's chapters and 
    end-of-chapter exercises. Information about the book is available at 
    <http://www.DesigningExperiments.com>.
	"""
	
	cran = "AMCP" 

	version("1.0.1", md5="4df924fae9c35945355d15a53f8be48d")

	depends_on("r@3:", type=("build", "run"))
