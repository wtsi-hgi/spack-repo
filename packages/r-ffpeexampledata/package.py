# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFfpeexampledata(RPackage):
	"""Illumina DASL example microarray data

	A subset of GSE17565 (April et al. 2009) containing 32 FFPE samples of Burkitts Lymphoma and Breast Adenocarcinoma, with a dilution series in technical duplicate.
	"""
	
	bioc = "ffpeExampleData"

	version("1.46.0", commit="5301acfd139bdf892b0b666c19195439043775f2")
	version("1.40.0", commit="50a7db785db872f21f020bc1e5e39bfd329a13fc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lumi", type=("build", "run"))

