# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAhmassbank(RPackage):
	"""MassBank Annotation Resources for AnnotationHub

	Supplies AnnotationHub with MassBank metabolite/compound annotations bundled in CompDb SQLite databases. CompDb SQLite databases contain general compound annotation as well as fragment spectra representing fragmentation patterns of compounds' ions. MassBank data is retrieved from https://massbank.eu/MassBank and processed using helper functions from the CompoundDb Bioconductor package into redistributable SQLite databases.
	"""
	
	homepage = "https://github.com/jorainer/AHMassBank"
	bioc = "AHMassBank" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/AHMassBank_1.2.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/AHMassBank/AHMassBank_1.2.1.tar.gz"]

	version("1.2.1", md5="71a167eaf9e590b5ec3574dff9658df6")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-annotationhubdata@1.5.24:", type=("build", "run"))
