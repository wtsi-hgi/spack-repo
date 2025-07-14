# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCuratedadipoarray(RPackage):
	"""A Curated Microarrays Dataset of MDI-induced Differentiated Adipocytes (3T3-L1) Under Genetic and Pharmacological Perturbations

	A curated dataset of Microarrays samples. The samples are MDI- induced pre-adipocytes (3T3-L1) at different time points/stage of differentiation under different types of genetic (knockdown/overexpression) and pharmacological (drug treatment) perturbations. The package documents the data collection and processing. In addition to the documentation, the package contains the scripts that was used to generated the data.
	"""
	
	homepage = "https://github.com/MahShaaban/curatedAdipoArray"
	bioc = "curatedAdipoArray"

	version("1.20.0", commit="34959184a85f2ccf0b3a823383f82c69286eff49")
	version("1.14.0", commit="78aa4dbacd1f24c00c4bd2a80227c922287aee63")

	depends_on("r@4:", type=("build", "run"))

