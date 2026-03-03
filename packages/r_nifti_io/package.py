# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNiftiIo(RPackage):
	"""Read and Write NIfTI Files

	Tools for reading and writing NIfTI-1.1 (NII) files, including optimized voxelwise read/write operations and a simplified method to write dataframes to NII.
    Specification of the NIfTI-1.1 format can be found here <https://nifti.nimh.nih.gov/nifti-1>.
    Scientific publication first using these tools
        Koscik TR, Man V, Jahn A, Lee CH, Cunningham WA (2020) <doi:10.1016/j.neuroimage.2020.116764> "Decomposing the neural pathways in a simple, value-based choice." Neuroimage, 214, 116764. 
	"""
	
	cran = "nifti.io" 

	version("1.0.0", md5="1a49895b3652be91b931041c79936dde")

	depends_on("r@3.5:", type=("build", "run"))
