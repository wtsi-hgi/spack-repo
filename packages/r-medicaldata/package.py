# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMedicaldata(RPackage):
	"""Data Package for Medical Datasets

	Provides access to well-documented medical datasets for teaching.
    Featuring several from the Teaching of Statistics in the Health Sciences 
    website <https://www.causeweb.org/tshs/category/dataset/>, a few reconstructed datasets of historical significance in medical
    research, some reformatted and extended from existing R packages, 
    and some data donations. 
	"""
	
	homepage = "https://higgi13425.github.io/medicaldata/"
	cran = "medicaldata" 

	version("0.2.0", md5="c810ef10272a451b770d741c79ae0db4")

	depends_on("r@3.1:", type=("build", "run"))
