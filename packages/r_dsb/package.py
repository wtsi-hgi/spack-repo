# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDsb(RPackage):
	"""Normalize & Denoise Droplet Single Cell Protein Data (CITE-Seq)

	This lightweight R package provides a method for normalizing and denoising protein expression data from droplet based single cell experiments. Raw protein Unique Molecular Index (UMI) counts from sequencing DNA-conjugated antibody derived tags (ADT) in droplets (e.g. 'CITE-seq') have substantial measurement noise. Our experiments and computational modeling revealed two major components of this noise: 1) protein-specific noise originating from ambient, unbound antibody encapsulated in droplets that can be accurately inferred via the expected protein counts detected in empty droplets, and 2) droplet/cell-specific noise revealed via the shared variance component associated with isotype antibody controls and background protein counts in each cell. This package normalizes and removes both of these sources of noise from raw protein data derived from methods such as 'CITE-seq', 'REAP-seq', 'ASAP-seq', 'TEA-seq', 'proteogenomic' data from the Mission Bio platform, etc. See the vignette for tutorials on how to integrate dsb with 'Seurat' and 'Bioconductor' and how to use dsb in 'Python'. Please see our paper Mulè M.P., Martins A.J., and Tsang J.S. Nature Communications 2022 <https://www.nature.com/articles/s41467-022-29356-8> for more details on the method.
	"""
	
	homepage = "https://github.com/niaid/dsb"
	cran = "dsb" 

	version("1.0.3", md5="6373c72a77f45ee7d3460ea10de02c4f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
