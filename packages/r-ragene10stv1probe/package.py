# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRagene10stv1probe(RPackage):
	"""Probe sequence data for microarrays of type ragene10stv1

	This package was automatically created by package AnnotationForge version 1.11.21. The probe sequence data was obtained from http://www.affymetrix.com. The file name was RaGene-1_0-st-v1_probe_tab.
	"""
	
	bioc = "ragene10stv1probe" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ragene10stv1probe_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ragene10stv1probe/ragene10stv1probe_2.18.0.tar.gz"]

	version("2.18.0", md5="94978b6efb075aacf31ccdc8000e40fa")

	depends_on("r@1.6:", type=("build", "run"))
	depends_on("r-annotationdbi@1.11.21:", type=("build", "run"))

