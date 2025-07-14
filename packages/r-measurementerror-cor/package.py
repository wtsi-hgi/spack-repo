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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MeasurementError.cor_1.74.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MeasurementError.cor/MeasurementError.cor_1.74.0.tar.gz"]

    version("1.80.0", tag="RELEASE_3_21")
	version("1.74.0", sha256="2e7631fb9bbf651651d983066173f235aa668638ab882f1e983df16b0468ec42")

