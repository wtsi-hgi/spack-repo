# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQcsis(RPackage):
	"""Sure Independence Screening via Quantile Correlation and
Composite Quantile Correlation

	Quantile correlation-sure independence screening (QC-SIS) and composite quantile correlation-sure independence screening (CQC-SIS) for ultrahigh-dimensional data.
	"""
	
	homepage = "http://www.r-project.org"
	cran = "QCSIS" 

	version("0.1", md5="23d614bef225f6180e4c335a1fc24197")

