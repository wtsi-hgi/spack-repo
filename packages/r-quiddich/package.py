# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuiddich(RPackage):
	"""QUick IDentification of DIagnostic CHaracters

	Provides tools for an automated identification of diagnostic molecular characters, i.e. such columns in a given nucleotide or amino acid alignment that allow to distinguish taxa from each other. These characters can then be used to complement the formal descriptions of the taxa, which are often based on morphological and anatomical features. Especially for morphologically cryptic species, this will be helpful. QUIDDICH distinguishes between four different types of diagnostic characters. For more information, see "Kuehn, A.L., Haase, M. 2019. QUIDDICH: QUick IDentification of DIagnostic CHaracters."
	"""
	
	cran = "quiddich" 

	version("1.0.0", md5="b1aecef6802083ab4026e33b86c2ae93")

	depends_on("r-ape@5.2:", type=("build", "run"))
	depends_on("r@0.12:", type=("build", "run"))
