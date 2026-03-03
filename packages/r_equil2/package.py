# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REquil2(RPackage):
	"""Calculate Urinary Saturation with the EQUIL2 Algorithm

	Saturation of ionic substances in urine is calculated based on
  sodium, potassium, calcium, magnesium, ammonia, chloride, phosphate, sulfate,
  oxalate, citrate, ph, and urate.  This program is intended for research use,
  only.  The code within is translated from EQUIL2 Visual Basic code based on
  Werness, et al (1985) "EQUIL2: a BASIC computer program for the calculation
  of urinary saturation" <doi:10.1016/s0022-5347(17)47703-2> to R. The Visual
  Basic code was kindly provided by Dr. John Lieske of the Mayo Clinic.
	"""
	
	homepage = "https://billdenney.github.io/equil2/"
	cran = "equil2" 

	version("1.0.0", md5="25f00420907f6ee3e4a26362d602a892", url="https://cran.r-project.org/src/contrib/equil2_1.0.0.tar.gz")

	depends_on("r-units", type=("build", "run"))
