# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatelife(RPackage):
	"""Scientific Data on Time of Lineage Divergence for Your Taxa

	Methods and workflows to get chronograms (i.e., phylogenetic trees with branch lengths
    proportional to time), using open, peer-reviewed, state-of-the-art scientific data on time of lineage divergence.
    This package constitutes the main underlying code of the DateLife web service
    at <https://www.datelife.org>. To obtain a single summary chronogram from a group of
    relevant chronograms, we implement the Super Distance Matrix (SDM) method
    described in Criscuolo et al. (2006) <doi:10.1080/10635150600969872>.
    To find the grove of chronograms with a sufficiently overlapping set of taxa
    for summarizing, we implement theorem 1.1. from Ané et al. (2009)
    <doi:10.1007/s00026-009-0017-x>.
    A given phylogenetic tree can be dated using time of lineage divergence data
    as secondary calibrations (with caution, see Schenk (2016) <doi:10.1371/journal.pone.0148228>).
    To obtain and apply secondary calibrations, the package implements the congruification method described
    in Eastman et al. (2013) <doi:10.1111/2041-210X.12051>. Tree dating can be performed with different methods
    including BLADJ (Webb et al. (2008) <doi:10.1093/bioinformatics/btn358>), PATHd8
    (Britton et al. (2007) <doi:10.1080/10635150701613783>), mrBayes (Huelsenbeck
    and Ronquist (2001) <doi:10.1093/bioinformatics/17.8.754>), and treePL (Smith
    and O'Meara (2012) <doi:10.1093/bioinformatics/bts492>).
	"""
	
	homepage = "https://github.com/phylotastic/datelife"
	cran = "datelife" 

	version("0.6.8", md5="fa86bfa50e6a9473acf8cdc03666ba19")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-bold", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-ips", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-compare", type=("build", "run"))
	depends_on("r-geiger", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rotl", type=("build", "run"))
	depends_on("r-paleotree", type=("build", "run"))
	depends_on("r-knitcitations", type=("build", "run"))
	depends_on("r-phylobase", type=("build", "run"))
	depends_on("r-taxize", type=("build", "run"))
	depends_on("r-treebase", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-phylocomr", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
