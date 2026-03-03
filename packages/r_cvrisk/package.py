# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCvrisk(RPackage):
	"""Compute Risk Scores for Cardiovascular Diseases

	Calculate various cardiovascular disease risk scores from the
    Framingham Heart Study (FHS), the American College of Cardiology (ACC),
    and the American Heart Association (AHA) as described in D’agostino, et al
    (2008) <doi:10.1161/circulationaha.107.699579>, Goff, et al (2013)
    <doi:10.1161/01.cir.0000437741.48606.98>, and Mclelland, et al (2015)
    <doi:10.1016/j.jacc.2015.08.035>.
	"""
	
	homepage = "https://github.com/vcastro/CVrisk"
	cran = "CVrisk" 

	version("1.1.1", md5="fde650b14af4f4888036a740783dae3b")

	depends_on("r@2.10:", type=("build", "run"))
