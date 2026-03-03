# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyGimmemotifs(PythonPackage):
    """GimmeMotifs is a motif prediction pipeline."""

    homepage = "https://github.com/vanheeringen-lab/gimmemotifs/"
    pypi = "gimmemotifs/gimmemotifs-0.9.0.3.tar.gz"

    version("0.10.0b1", sha256="156f315a70aba97fa2de291adb34c6470b54200e52bd019e12a43969ae9f1b54")
    version("0.10.0b2", sha256="5a633f386f89dfe434c86f1a971ef0d14ecfda8aa9fd25ac9e1542943d1edd97")
    version("0.10.0b4", sha256="2662e2004ebe948666e02f850e0e42171e195edf6e0b569f8eed4fb478154b49")
    version("0.10.0b5", sha256="6a2ea4bee04d65f062569f18962bd9e7f579289edb328d1c3fa246f7ef7368f3")
    version("0.10.0b6", sha256="058d19e174c474dda84ff2e20a347553ef483cb9d4d22d2a1117620698b99376")
    version("0.11.0", sha256="bea23d41cecb19e64a0df0acbe41912b20cf9e553a968df058d51f33f45ecc9e")
    version("0.11.0b0", sha256="33f2362a3dc0806846fb5789edf5ae8546142162998d3ba0f2090c8eaf6311ea")
    version("0.11.1", sha256="b24498e9e09f238fa6ac13f1c0d4ae69425062a63aec875de5cb45b907bc5915")
    version("0.12.0", sha256="5d77d7d30ca5432388dd70e1975012333d2aebe05acf2b341ccd3c6c1cc71214")
    version("0.13.0", sha256="7db82ff0a0c85d3ba2a331d1a4721a715ae5aab13f96aceb48fe23945d179ed4")
    version("0.13.1", sha256="64593fa757171b361e5dfd3a70fc610d792078648cd164d19c84dc4f156004b0")
    version("0.14.0", sha256="115157c3c04e43c94e110ce1d7e46b2a1cbfcdda31b737542e73c9fe22318df0")
    version("0.14.2", sha256="a34834c775b92a6ce0d95725bf1ec72e3b200645ecd3c9c5b12acc70e5913be0")
    version("0.14.3", sha256="e83e4a0187753c6310041e5cb9382e9fea3dbb9bb72c431ca3d1989bf0ccd984")
    version("0.14.4", sha256="1b9a0edb2051c90336a430a67bfdd4ec809ef0ce00ba6f4e0be5d62b9fe0904c")
    version("0.15.0", sha256="7c6e704b5d91484c0120f26bb3d7b60675a042f171d4e83a32d3fadc643196fa")
    version("0.15.2", sha256="16939bbd23f6f0f6fd79a980ff914ab5b7e8fa7c1f02f2e86c02979f4fdf8f6a")
    version("0.15.3", sha256="9ee7eb435076fb5dc8496e7a91b767f11537a0f0eb4915749c63d52c265dd72d")
    version("0.16.0", sha256="41c890f2cc097ef4be6cf82601d4789cb79fff168f977a72155782cc9b91a3b0")
    version("0.17.0", sha256="9bec8833f32376c6f51f7add361789bfb65adc7cbb03897d9eb8ead03645152a")
    version("0.17.2", sha256="fbf70997abce6a75451c10b96994f8dbc03152b01df5cf30bf4397c98a9b54d2")
    version("0.18.0", sha256="94f1f4f642f1a981598003254ed207a9d22716111f556e78bbe1ab709cc4d3a7")
    version("0.8.9.1", sha256="d0ef7814744c203003fee7cddd40b3a251708d788901a58c4e49f8ebd3d3967a")
    version("0.9.0.2", sha256="067517aab6c199031c98501adbba07cefbf3af51788f5cafde9c49e41ca9860e")
    version("0.9.0.3", sha256="19fd267ed30fd90a727c7bb99bd89bd0cd16c11fa3a2cfb29e9da219a23cf568")

    depends_on("py-setuptools", type=("build"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-seaborn", type=("build", "run"))
    depends_on("py-genomepy", type=("build", "run"))
    depends_on("py-scikit-learn", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-pysam", type=("build", "run"))
    depends_on("py-pybedtools", type=("build", "run"))
    depends_on("py-pyfaidx", type=("build", "run"))
    depends_on("py-statsmodels", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-feather-format", type=("build", "run"))
    depends_on("py-biofluff", type=("build", "run"))
    depends_on("py-ipywidgets", type=("build", "run"))
    depends_on("py-iteround", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))
    depends_on("py-logomaker", type=("build", "run"))
    depends_on("py-loguru", type=("build", "run"))
    depends_on("py-xxhash", type=("build", "run"))
    depends_on("py-qnorm", type=("build", "run"))
    depends_on("py-xdg", type=("build", "run"))

    def patch(self):
        filter_file("SafeConfigParser", "ConfigParser", "versioneer.py", string=True)
        filter_file("readfp", "read_file", "versioneer.py", string=True)
