# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrecisetad(RPackage):
	"""preciseTAD: A machine learning framework for precise TAD boundary prediction

	preciseTAD provides functions to predict the location of boundaries of topologically associated domains (TADs) and chromatin loops at base-level resolution. As an input, it takes BED-formatted genomic coordinates of domain boundaries detected from low-resolution Hi-C data, and coordinates of high-resolution genomic annotations from ENCODE or other consortia. preciseTAD employs several feature engineering strategies and resampling techniques to address class imbalance, and trains an optimized random forest model for predicting low-resolution domain boundaries. Translated on a base-level, preciseTAD predicts the probability for each base to be a boundary. Density-based clustering and scalable partitioning techniques are used to detect precise boundary regions and summit points. Compared with low-resolution boundaries, preciseTAD boundaries are highly enriched for CTCF, RAD21, SMC3, and ZNF143 signal and more conserved across cell lines. The pre-trained model can accurately predict boundaries in another cell line using CTCF, RAD21, SMC3, and ZNF143 annotation data for this cell line.
	"""
	
	homepage = "https://github.com/dozmorovlab/preciseTAD"
	bioc = "preciseTAD"

	version("1.18.0", commit="1ff553cd858851980a4a05198ea08ddc7d42ebd4")
	version("1.12.0", commit="a64ffb7e114677d9be5a9d331cddcc792e3f1d06")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-modelmetrics", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-prroc", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-rcgh", type=("build", "run"))
