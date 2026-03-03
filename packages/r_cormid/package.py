# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCormid(RPackage):
	"""Correct Mass Isotopologue Distribution Vectors

	In metabolic flux experiments tracer molecules (often glucose
    containing labelled carbon) are incorporated in compounds measured
    using mass spectrometry. The mass isotopologue distributions of these
    compounds needs to be corrected for natural abundance of labelled
    carbon and other effects, which are specific on the compound and
    ionization technique applied. This package provides functions to
    correct such effects in gas chromatography atmospheric pressure
    chemical ionization mass spectrometry analyses.
	"""
	
	homepage = "https://github.com/janlisec/CorMID"
	cran = "CorMID" 

	version("0.1.9", md5="f8e759512add8e2ed48682a52240ee71")

	depends_on("r@3.50:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rdisop", type=("build", "run"))
