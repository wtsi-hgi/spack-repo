# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProdlim(RPackage):
	"""Product-Limit Estimation for Censored Event History Analysis.

	Product-Limit Estimation for Censored Event History Analysis. Fast and user
	friendly implementation of nonparametric estimators for censored event
	history (survival) analysis. Kaplan-Meier and Aalen-Johansen method."""

	cran = "prodlim"
	version("2023.08.28", md5="659174e40f0c8061d3312aa09464a838")
	version("1.6.1", sha256="3f2665257118a3db8682731a500b1ae4d669af344672dc2037f987bee3cca154")
	version("1.5.9", sha256="853644886c57102e7f6dd26b6e03e54bf3f9e126f54c76f8d63a3324811f7b42")
	version(
		"2023.03.31", sha256="5510454f8511ca956666f27dfb77d875c56b9166188c33f22cd22b7615797800"
	)
		"2019.11.13", sha256="6809924f503a14681de84730489cdaf9240d7951c64f5b98ca37dc1ce7809b0f"
	)
		"2018.04.18", sha256="4b22b54fdf712439309be0ff74f63cde9080464667b00e19823372ac0fc254ab"
	)

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-diagram", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-lava", type=("build", "run"))
