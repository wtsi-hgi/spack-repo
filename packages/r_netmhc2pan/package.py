# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetmhc2pan(RPackage):
	"""Interface to 'NetMHCIIpan'

	The field of immunology benefits from software that can
    predict which peptide sequences trigger an immune response.
    'NetMHCIIpan' is a such a tool: it predicts the
    binding strength of a short peptide to a Major Histocompatibility
    Complex class II (MHC-II) molecule.
    'NetMHCIIpan' can be used from a web server at 
    <https://services.healthtech.dtu.dk/services/NetMHCIIpan-3.2/>
    or from the command-line, using a local installation. This package
    allows to call 'NetMHCIIpan' from R.
	"""
	
	homepage = "https://github.com/richelbilderbeek/netmhc2pan/"
	cran = "netmhc2pan" 

	version("1.3.2", md5="1f1c591664cee721e8e9eb2a35333038")

	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-testit", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
