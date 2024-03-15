# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPepxmltab(RPackage):
	"""Parsing pepXML files and filter based on peptide FDR.

	Parsing pepXML files based one XML package. The package tries to handle pepXML files generated from different softwares. The output will be a peptide-spectrum-matching tabular file. The package also provide function to filter the PSMs based on FDR.
	"""
	
	bioc = "pepXMLTab" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/pepXMLTab_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/pepXMLTab/pepXMLTab_1.36.0.tar.gz"]

	version("1.36.0", md5="71d6bcb41c5a79bc2cfdd375c6468250")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-xml@3.98.1.1:", type=("build", "run"))
