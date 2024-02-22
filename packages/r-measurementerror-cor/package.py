# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeasurementerrorCor(RPackage):
	"""Measurement Error model estimate for correlation coefficient

	Two-stage measurement error model for correlation estimation with smaller bias than the usual sample correlation
	"""
	
	bioc = "MeasurementError.cor" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MeasurementError.cor_1.74.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MeasurementError.cor/MeasurementError.cor_1.74.0.tar.gz"]

	version("1.74.0", md5="7de3f5ca3749a7b1e80fdfa66204a252")

