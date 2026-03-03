# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKlausur(RPackage):
	"""Multiple Choice Test Evaluation

	A set of functions designed to quickly generate results of a multiple choice
          test. Generates detailed global results, lists for anonymous feedback and
          personalised result feedback (in LaTeX and/or PDF format), as well as item
          statistics like Cronbach's alpha or disciminatory power. 'klausuR' also
          includes a plugin for the R GUI and IDE RKWard, providing graphical dialogs for
          its basic features. The respective R package 'rkward' cannot be installed
          directly from a repository, as it is a part of RKWard. To make full use of this
          feature, please install RKWard from <https://rkward.kde.org> (plugins are
          detected automatically). Due to some restrictions on CRAN, the full package
          sources are only available from the project homepage.
	"""
	
	homepage = "https://reaktanz.de/?c=hacking&s=klausuR"
	cran = "klausuR" 

	version("0.12-14", md5="898d2da40a38b2dadea8d34016ff2645")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
