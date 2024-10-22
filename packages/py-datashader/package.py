# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDatashader(PythonPackage):
    """Datashader is a graphics pipeline system for creating meaningful representations of large datasets quickly and flexibly. Datashader breaks the creation of images into a series of explicit steps that allow computations to be done on intermediate representations. This approach allows accurate and effective visualizations to be produced automatically without trial-and-error parameter tuning, and also makes it simple for data scientists to focus on particular data and relationships of interest in a principled way."""

    homepage = "https://datashader.org/"
    pypi = "datashader/datashader-0.13.0.tar.gz"

    version("0.16.3", sha256="9d0040c7887f7a5a5edd374c297402fd208a62bf6845e87631b54f03b9ae479d")
    version("0.13.0", sha256="e89b1c1e6d508c399738b2daf37aa102f63fc70be53cce9db90d654b19c2555f")

    depends_on("py-hatchling", type="build")
    depends_on("py-hatch-vcs", type="build")

    depends_on("py-colorcet", type=("build", "run"))
    depends_on("py-dask", type=("build", "run"))
    depends_on("py-llvmlite", type=("build", "run"))
    depends_on("py-multipledispatch", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-param", type=("build", "run"))
    depends_on("py-pillow", type=("build", "run"))
    depends_on("py-pyct", type=("build", "run"))
    depends_on("py-requests", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-toolz", type=("build", "run"))
    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-xarray", type=("build", "run"))
