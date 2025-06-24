# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPlacer(BundlePackage):
    """Protein-Ligand Atomistic Conformational Ensemble Resolver (PLACER).

    PLACER is a graph neural network that operates entirely at the atomic level;
    the nodes of the graph are the atoms in the system. PLACER was trained to
    recapitulate the correct atom positions from partially corrupted input structures
    from the Cambridge Structural Database and the Protein Data Bank. PLACER accurately
    generates structures of diverse organic small molecules given knowledge of their
    atom composition and bonding, and given a description of the larger protein context,
    can accurately build up structures of small molecules and protein side chains."""

    homepage = "https://github.com/baker-laboratory/PLACER"

    license("BSD-3-Clause")

    version("20250307")

    # Build dependencies
    depends_on("py-setuptools", type="build")
    depends_on("py-wheel", type="build")
    depends_on("py-pip", type="build")

    # Core scientific computing dependencies
    depends_on("py-numpy@1.20.0:", type=("build", "run"))
    depends_on("py-pandas@2.2.0:", type=("build", "run"))
    depends_on("py-scipy@1.7.0:", type=("build", "run"))
    depends_on("py-networkx@3.2:", type=("build", "run"))

    # Deep learning dependencies
    depends_on("py-torch@2.3.0:2.3+cuda", type=("build", "run"))
    depends_on("py-dgl@2.4.0", type=("build", "run"))
    depends_on("py-e3nn@0.5.4", type=("build", "run"))
    depends_on("py-opt-einsum@3.3.0:", type=("build", "run"))
    depends_on("py-se3-transformer", type=("build", "run"))

    # Chemistry and molecular modeling dependencies
    depends_on("openbabel@3.1.1", type=("build", "run"))

    # Optional convenience dependencies
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-ipython", type=("build", "run"))
    depends_on("py-jupyterlab", type=("build", "run"))
    
    # Additional Python dependencies for molecular modeling
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))

    # CUDA dependencies
    depends_on("cuda@12.1:", type=("build", "run"))
    depends_on("cudnn", type=("build", "run")) 