# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install r-configr
#
# You can edit this file again by typing:
#
#     spack edit r-configr
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RConfigr(RPackage):
    """Implements the JSON, INI, YAML and TOML parser for R setting and writing of configuration file. The functionality of this package is similar to that of package 'config'."""

    homepage = "https://github.com/Miachol/configr"
    cran = "configr"

    version("0.3.5", sha256="43a19fa4920f2265ac4b2e03de36c5e135d1c97dfdc1fecee0b061ee92fa8ee2")
    version("0.3.4", sha256="3a0ec2455706416bb5fc5b1a8079619927eb8aa8218c4a742b89ad59d72c5c73")
    version("0.3.3", sha256="a283635e688be27f326c98adc1229087c07c1a3377a194f6aa660a283501ca21")
    version("0.3.2.2", sha256="9ff3d82aa6fef60614e8c3e6f288f779b8e019353b05a62064fb6c6df6400899")
    version("0.3.2.1", sha256="c1e2f1e6a1023f141ab1fcabe0c93cb8556cb503e09d832c896802a99b5391a0")
    version("0.3.2", sha256="99958d4878cf9d1c58de4ec267d10651bf6d85e1a254ab9da4ed98e06f6f8f84")
    version("0.3.1.1", sha256="6d9db2c4ba3a2d10f2574113c09d82573f8f2b9543cd840a8cf7eb7a8fba6a9c")
    version("0.3.1", sha256="bbd3d67c6103951397dbaf199f3bc40c993cae49133036fefc81e812043f148a")
    version("0.3.0", sha256="aab405f5f4f87814341334e8edb9c25162ab63ca1b677513bb1c075ed50d0923")
    version("0.2.3", sha256="9579de8ed66cb204e9e2e3886cbd6e706905d60e2c7aab280064384d7ac722de")
    version("0.2.2", sha256="2114fa8acbb7913d19945b2febbe80520bf5c12c7d90fcb22d439cede39daf6f")
    version("0.2.1", sha256="1ae0b66a1c4dc226f89aa85f09820b22b71b2cb19eba47d6a8e15e6a2d9cb52c")
    version("0.2.0", sha256="25edbc335862c6afb1ed13b697869e249c893112cd1ebe6761f94d8cf265a465")
    version("0.1.0", sha256="ec6f191bfdcc85ad83f51e6a1e2889b7c25babe9425138291d570899d8c05279")
    version("0.0.3", sha256="dac65f9069ed751735a591819a035b3ed045be37a5cef0458787db69fd41861e")
    version("0.0.2", sha256="9df159aacfda7a205e5eb45e61fcbbfbeb5faf521c0597beaf0631a345b8214f")

    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-ini", type=("build", "run"))
    depends_on("r-yaml", type=("build", "run"))
    depends_on("r-rcpptoml", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-glue", type=("build", "run"))
