# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRncl(RPackage):
	"""An Interface to the Nexus Class Library.

	An interface to the Nexus Class Library which allows parsing of NEXUS,
	Newick and other phylogenetic tree file formats. It provides elements of
	the file that can be used to build phylogenetic objects such as ape's
	'phylo' or phylobase's 'phylo4(d)'. This functionality is demonstrated with
	'read_newick_phylo()' and 'read_nexus_phylo()'."""

	cran = "rncl"

	version("0.8.10", sha256="8c80ee535786a0bb4b87e27a89dc77b7ef5a4ac1427b5d48e6e8f4652e16db85")
	version("0.8.9", sha256="8e64a0cae60010498e3aa7a858f1b18143ae2e0eff0ed7db0a76bcda05012709")
	version("0.8.8", sha256="85e3ebba702131cf43e272af977182c88e4ea5d9d940f50d9ed3f02fee7e0d2f")
	version("0.8.7", sha256="1d876e4f5f2b8a24cc3ea1002c29eedbc0ca96011b0fa15b085e5b75cfc7993a")
	version("0.8.6", sha256="fcc972c04fb43ace0876eb640a6433caddf6ec8304f7ceee37107d812ce68ffb")
	version("0.8.4", sha256="6b19d0dd9bb08ecf99766be5ad684bcd1894d1cd9291230bdd709dbd3396496b")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-rcpp@0.11.0:", type=("build", "run"))
	depends_on("r-rcpp@:1.0", type=("build", "run"), when="@:0.8.7")
	depends_on("r-progress@1.1.2:", type=("build", "run"))
