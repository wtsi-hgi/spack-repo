# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmPluginKorpus(RPackage):
	"""Full Corpus Support for the 'koRpus' Package

	Enhances 'koRpus' text object classes and methods to also support large
          corpora. Hierarchical ordering of corpus texts into arbitrary categories will
          be preserved. Provided classes and methods also improve the ability of using
          the 'koRpus' package together with the 'tm' package. To ask for help, report
          bugs, suggest feature improvements, or discuss the global development of the
          package, please subscribe to the koRpus-dev mailing list
          (<https://korpusml.reaktanz.de>).
	"""
	
	homepage = "https://reaktanz.de/?c=hacking&s=koRpus"
	cran = "tm.plugin.koRpus" 

	version("0.4-2", md5="408433b2def4785461ad3790d5bc3fab")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-korpus@0.13.1:", type=("build", "run"))
	depends_on("r-sylly@0.1.6:", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-nlp", type=("build", "run"))
