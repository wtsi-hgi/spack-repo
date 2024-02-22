# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhenorm(RPackage):
	"""Unsupervised Gold-Standard Label Free Phenotyping Algorithm for
EHR Data

	The algorithm combines the most predictive variable, such as count of the main International Classification of Diseases (ICD) codes, and other Electronic Health Record (EHR) features (e.g. health utilization and processed clinical note data), to obtain a score for accurate risk prediction and disease classification. In particular, it normalizes the surrogate to resemble gaussian mixture and leverages the remaining features through random corruption denoising. Background and details about the method can be found at Yu et al. (2018) <doi:10.1093/jamia/ocx111>.
	"""
	
	homepage = "https://github.com/celehs/PheNorm"
	cran = "PheNorm" 

	version("0.1.0", md5="139c0a12960913e2cda7ab0ca0b73818")

