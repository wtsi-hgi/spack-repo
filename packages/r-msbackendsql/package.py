# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsbackendsql(RPackage):
	"""SQL-based Mass Spectrometry Data Backend

	SQL-based mass spectrometry (MS) data backend supporting also storange and handling of very large data sets. Objects from this package are supposed to be used with the Spectra Bioconductor package. Through the MsBackendSql with its minimal memory footprint, this package thus provides an alternative MS data representation for very large or remote MS data sets.
	"""
	
	homepage = "https://github.com/RforMassSpectrometry/MsBackendSql"
	bioc = "MsBackendSql" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MsBackendSql_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MsBackendSql/MsBackendSql_1.2.0.tar.gz"]

	version("1.2.0", sha256="40c5538d884b82603ecb7f1b0e0fa2ad49ba4849eda48ad6be0f7af6ae2788c8")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-spectra@1.9.12:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-protgenerics", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-mscoreutils", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
