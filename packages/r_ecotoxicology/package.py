# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcotoxicology(RPackage):
	"""Methods for Ecotoxicology

	Implementation of the EPA's Ecological Exposure Research Division (EERD) tools (discontinued in 1999) for Probit and Trimmed Spearman-Karber Analysis.
    Probit and Spearman-Karber methods from Finney's book "Probit analysis a statistical treatment of the sigmoid response curve" with options for most accurate results or identical results to the book.
    Probit and all the tables from Finney's book (code-generated, not copied) with the generating functions included.
    Control correction: Abbott, Schneider-Orelli, Henderson-Tilton, Sun-Shepard.
    Toxicity scales: Horsfall-Barratt, Archer, Gauhl-Stover, Fullerton-Olsen, etc.
	"""
	
	cran = "ecotoxicology" 

	version("1.0.1", md5="5885ec7d98b7dc50cbd57e97701af316")

	depends_on("r@2.10:", type=("build", "run"))
