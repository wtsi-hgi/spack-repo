# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyQmplot(PythonPackage):
    """qmplot: Create high-quality manhattan and QQ plots for PLINK association output (or any dataframe with chromosome, position, and p-value)."""

    homepage = "https://github.com/ShujiaHuang/qmplot"
    pypi = "qmplot/qmplot-0.3.3.tar.gz"

    version("0.0.1", sha256="59b557df16198ae1ea9d4a735e4a6b84145acc458f065bc82aa8cd4967028408")
    version("0.0.2", sha256="4ccbc3f0c2fcda8c4d8f2fdcb0b6c50b0d804de1cd7eef4df8fbd6200128c54d")
    version("0.0.4", sha256="c5b49f65a754f8b7f3a1af1015704e3715d1e67d4e6a37f920c37f442130a3c9")
    version("0.0.5", sha256="2331e5d2670a3fd574425d9ec0df2033984f7a1dfb2358f6ce8ba189f28e4e71")
    version("0.0.6", sha256="4f6ce13ba09a25bad080c6a731517675bdf915e91e89aca7bff4b79b7c3b35d5")
    version("0.0.7", sha256="1799c90b930dd5f4bc2a18bfc5ed790a25ed85807fc8cdec29429109e20fdb1e")
    version("0.0.8", sha256="5615a52aa68384a32d6bf930c06d1d7ef157f90da0023344f66920893f8ba928")
    version("0.1.0", sha256="845260204054a34effbeb6c1093827167d0fdf86a63c76b1f6860c68f4024b5b")
    version("0.1.1", sha256="c527d78bdc5f95e2f5d274e0eb7f0168d09fc4bae003d9e7c76c2f1fb1c81c15")
    version("0.1.2", sha256="a99e4b1a3d74af099d5cf1e7e97cfdfa9ee48188011cdbba4baf22f7931b6faa")
    version("0.1.3", sha256="d73fb4131b1200002a0ed965664461921d1b2fbd448b432318aad77b8247016a")
    version("0.1.4", sha256="f5ad9b280551de061ef546fab513c9850456d157d7d79dc4aa3e5db1a848b9bb")
    version("0.1.5", sha256="8b9caa7f2b988276e451282afb763f1745ca0a554d765d60788afa52835c5fe7")
    version("0.1.6", sha256="7af691ad37a1488978edae367cbc97a48dae958e506b0883d1b967466795344d")
    version("0.1.7", sha256="ca99337e8a300a460930ce4deb85dc194f93707505a27a09722fad8f520ab8d8")
    version("0.1.8", sha256="ae5a59e22e4a9703f560b71d2430fcf1c015a702031a90e7e31b9f0b86c828ea")
    version("0.2.0", sha256="67fb26b5ce8e0a364c03f8d60e80d0e68c7fbe720cdf766ae147a2b128e31fa5")
    version("0.2.1", sha256="cc515b822919847116412b1feaf00ac991340a081948053bd1b7de2fdf7cca6a")
    version("0.3.0", sha256="d5ab7791b427517d2219b4d4bdfb22e3797572d39566889d03903c1eec9709b8")
    version("0.3.1", sha256="9fdca631695e13dc26b6785e56b8437cfa7e95e6c2af26d0d6fd5ccdbf7a8511")
    version("0.3.2", sha256="5335ac66eeac9d2465cf40db8986d5ad200e13588febb24c4f6bc800bacd16ef")
    version("0.3.3", sha256="e19af15668c50b43da4cc424a7b0a18b784a88e0f578a3fd0344ef8cb22d532e")

    depends_on("py-setuptools", type=("build"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
