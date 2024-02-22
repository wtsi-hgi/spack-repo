# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKorpusLangEn(RPackage):
	"""Language Support for 'koRpus' Package: English

	Adds support for the English language to the 'koRpus' package. To ask for help, report bugs, suggest feature improvements, or discuss the global development of the
                    package, please consider subscribing to the koRpus-dev mailing list (<https://korpusml.reaktanz.de>).
	"""
	
	homepage = "https://reaktanz.de/?c=hacking&s=koRpus"
	cran = "koRpus.lang.en" 

	version("0.1-4", md5="480342a7aaef8b11a065c7d02240ddd6")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-korpus@0.11.2:", type=("build", "run"))
	depends_on("r-sylly-en", type=("build", "run"))
