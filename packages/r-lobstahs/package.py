# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLobstahs(RPackage):
	"""Lipid and Oxylipin Biomarker Screening through Adduct Hierarchy Sequences

	LOBSTAHS is a multifunction package for screening, annotation, and putative identification of mass spectral features in large, HPLC-MS lipid datasets. In silico data for a wide range of lipids, oxidized lipids, and oxylipins can be generated from user-supplied structural criteria with a database generation function. LOBSTAHS then applies these databases to assign putative compound identities to features in any high-mass accuracy dataset that has been processed using xcms and CAMERA. Users can then apply a series of orthogonal screening criteria based on adduct ion formation patterns, chromatographic retention time, and other properties, to evaluate and assign confidence scores to this list of preliminary assignments. During the screening routine, LOBSTAHS rejects assignments that do not meet the specified criteria, identifies potential isomers and isobars, and assigns a variety of annotation codes to assist the user in evaluating the accuracy of each assignment.
	"""
	
	homepage = "http://bioconductor.org/packages/LOBSTAHS"
	bioc = "LOBSTAHS" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/LOBSTAHS_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/LOBSTAHS/LOBSTAHS_1.28.0.tar.gz"]

	version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="cd685033832ebf0f439f6182a00b9d484fa5bcbf15adae129d5b4b18c8687e3d")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-xcms", type=("build", "run"))
	depends_on("r-camera", type=("build", "run"))
