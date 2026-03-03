# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSoniclength(RPackage):
	"""Estimating Abundance of Clones from DNA Fragmentation Data

	Estimate the abundance of cell clones from the
	     distribution of lengths of DNA fragments (as created by
	     sonication, whence `sonicLength').  The algorithm in
	     "Estimating abundances of retroviral insertion sites from
	     DNA fragment length data" by Berry CC, Gillet NA, Melamed
	     A, Gormley N, Bangham CR, Bushman FD. Bioinformatics;
	     2012 Mar 15;28(6):755-62 is implemented.  The
	     experimental setting and estimation details are described
	     in detail there. Briefly, integration of new DNA in a
	     host genome (due to retroviral infection or gene therapy)
	     can be tracked using DNA sequencing, potentially allowing
	     characterization of the abundance of individual cell
	     clones bearing distinct integration sites. The locations
	     of integration sites can be determined by fragmenting the
	     host DNA (via sonication or fragmentase), breaking the
	     newly integrated DNA at a known sequence, amplifying the
	     fragments containing both host and integrated DNA,
	     sequencing those amplicons, then mapping the host
	     sequences to positions on the reference genome. The
	     relative number of fragments containing a given position
	     in the host genome estimates the relative abundance of
	     cells hosting the corresponding integration site, but
	     that number is not available and the count of amplicons
	     per fragment varies widely.  However, the expected number
	     of distinct fragment lengths is a function of the
	     abundance of cells hosting an integration site at a given
	     position and a certain nuisance parameter. The algorithm
	     implicitly estimates that function to estimate the
	     relative abundance.
	"""
	
	cran = "sonicLength" 

	version("1.4.7", md5="f2ba331f3e7c0368220ec0c463d6838f")

	depends_on("r@2.14:", type=("build", "run"))
