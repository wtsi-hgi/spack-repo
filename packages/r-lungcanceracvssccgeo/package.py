# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLungcanceracvssccgeo(RPackage):
	"""A lung cancer dataset that can be used with maPredictDSC package for developing outcome prediction models from Affymetrix CEL files.

	This package contains 30 Affymetrix CEL files for 7 Adenocarcinoma (AC) and 8 Squamous cell carcinoma (SCC) lung cancer samples taken at random from 3 GEO datasets (GSE10245, GSE18842 and GSE2109) and other 15 samples from a dataset produced by the organizers of the IMPROVER Diagnostic Signature Challenge available from GEO (GSE43580).
	"""
	
	homepage = "http://bioinformaticsprb.med.wayne.edu/"
	bioc = "LungCancerACvsSCCGEO"

	version("1.44.0", commit="25b95b152f8f0bc06a1108cf6f284956fadb4f62")
	version("1.38.0", commit="1b119899e15211d760ccfef53888bb4fa26fd653")

	depends_on("r@2.15:", type=("build", "run"))

