# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSyllyEn(RPackage):
	"""Language Support for 'sylly' Package: English

	Adds support for the English language to the 'sylly'
        package. Due to some restrictions on CRAN, the full package
        sources are only available from the project homepage. To ask
        for help, report bugs, suggest feature improvements, or discuss
        the global development of the package, please consider
        subscribing to the koRpus-dev mailing list
        (<http://korpusml.reaktanz.de>).
	"""
	
	homepage = "http://reaktanz.de/?c=hacking&s=koRpus"
	cran = "sylly.en" 

	version("0.1-3", md5="85f15e0ddadf21a5c51171114a9aced8")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-sylly", type=("build", "run"))
