# -*- coding: utf-8 -*-
# HORTON: Helpful Open-source Research TOol for N-fermion systems.
# Copyright (C) 2011-2016 The HORTON Development Team
#
# This file is part of HORTON.
#
# HORTON is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# HORTON is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
#
# --

from numpy import array, allclose
from nose.plugins.attrib import attr

from horton import context


@attr('regression_check')
def test_rhf_n2_dense():
    ref_result_energy = -108.95408660509986
    ref_result_exp_alpha = array([[ -7.07296715e-01,  -7.08389687e-01,   8.64165974e-03,
         -3.47517494e-03,  -1.14436900e-02,  -7.95110009e-18,
          6.15354282e-17,   2.07196148e-16,  -2.14931167e-17,
          3.07566069e-02,  -1.57713606e-01,   5.70697477e-16,
         -1.24237249e-15,   4.27104890e-01,   1.15736737e-15,
         -3.79160016e-16,   1.45125097e-01,   6.47187332e-01,
         -3.24356740e-17,   1.98058266e-08,   1.57652597e-16,
         -1.43924318e-17,  -9.99370627e-15,  -6.43455604e-09,
          3.87021589e-01,  -1.63188579e-15,  -5.54912366e-16,
          1.80200661e-01],
       [ -3.82249923e-04,  -1.66259928e-03,  -3.34086476e-01,
         -3.27485529e-01,   9.61151106e-02,   1.14136682e-15,
          1.98709685e-16,   2.70967935e-16,  -6.67285545e-17,
         -1.68727992e-01,  -3.01626331e-01,   1.42385338e-15,
         -2.73204403e-15,   1.03853186e+00,   2.77843939e-15,
         -1.17423787e-15,   2.25810008e-01,   1.43833996e+00,
         -7.17245085e-17,   4.87802045e-08,   4.09410062e-16,
          3.77074889e-17,  -2.15307739e-14,  -1.38618916e-08,
          7.28242309e-01,  -3.01501407e-15,  -1.04828096e-15,
          4.81572779e-01],
       [  1.60307814e-03,   4.59916822e-03,  -1.94141431e-01,
         -4.21919705e-01,   3.30574419e-01,   1.33264103e-15,
         -4.38226539e-16,  -1.54420484e-15,   1.69017340e-17,
         -3.93920485e+00,   2.49674946e-03,  -3.83488223e-15,
          2.53721858e-15,  -9.33567630e-01,  -2.32904287e-15,
         -7.89820653e-16,  -6.43687511e-01,  -6.09012017e+00,
          2.95801569e-16,  -4.20834300e-08,   8.85567474e-16,
          1.61777945e-16,   8.88808360e-14,   5.72541112e-08,
         -3.29154883e-01,   1.37872340e-15,  -1.85851620e-16,
          3.21852717e+00],
       [  1.90615654e-17,  -1.39546639e-16,   2.98975321e-16,
          1.67364492e-15,   5.16038826e-17,   4.22744597e-01,
          5.58122666e-02,  -4.24107906e-01,   5.59922808e-02,
          5.76619433e-17,   1.42318153e-15,  -6.36852101e-01,
          8.40795869e-02,  -9.83084895e-16,   7.26344459e-01,
         -9.58946849e-02,   6.36661714e-16,   4.04406066e-16,
          1.52249212e-16,  -1.45436797e-17,  -2.86842953e-01,
          3.78700707e-02,  -1.34932740e-17,   3.84890558e-17,
          1.07830413e-15,   2.40896783e-01,   3.18041713e-02,
          2.98834902e-16],
       [  7.10582497e-18,  -1.82074507e-17,  -1.14910643e-16,
          1.53291610e-16,   9.16948537e-17,  -5.58123003e-02,
          4.22744342e-01,   5.59922936e-02,   4.24107809e-01,
         -2.03898008e-16,  -2.01635408e-15,   8.40795633e-02,
          6.36852280e-01,  -5.96838722e-16,  -9.58946779e-02,
         -7.26344513e-01,   1.17934378e-15,   2.86184358e-16,
          4.22000592e-16,   3.17238447e-17,   3.78700735e-02,
          2.86842932e-01,   1.90722885e-16,  -3.00834467e-17,
          4.99005008e-16,  -3.18041700e-02,   2.40896793e-01,
          3.33608568e-17],
       [ -1.37260556e-03,  -2.36276482e-03,  -2.17748589e-01,
          2.15878284e-01,  -4.54265589e-01,  -5.36470609e-16,
          1.20881346e-16,   5.80533490e-16,  -1.09294886e-16,
         -6.05578251e-02,  -4.60283493e-01,  -1.60320800e-15,
         -4.68718075e-16,  -2.69004274e-01,  -5.64867952e-16,
          4.34719209e-17,  -7.55769681e-01,   1.28194696e-01,
         -7.13797737e-18,   2.60732912e-09,  -4.20916332e-16,
          1.79743756e-16,   3.62358694e-16,   2.46057498e-10,
          3.66006395e-01,  -1.83040401e-15,  -6.44598642e-16,
          1.07198186e+00],
       [ -4.20659539e-19,  -1.84306910e-19,  -3.37168438e-17,
          8.99082665e-16,   7.52851315e-18,   2.54777432e-01,
          3.36366888e-02,  -6.71336935e-01,   8.86324028e-02,
          3.87619035e-16,  -2.11112350e-15,   6.14580834e-01,
         -8.11392149e-02,   2.35601663e-15,  -1.14717110e+00,
          1.51453754e-01,  -8.55066026e-16,  -3.35767230e-16,
         -8.64101899e-17,  -2.54585614e-18,   6.83991150e-02,
         -9.03030415e-03,   6.43708482e-17,  -2.03735211e-18,
          1.98379076e-15,   4.59492430e-01,   6.06640536e-02,
         -7.63778092e-17],
       [ -7.86907811e-19,  -4.90730578e-19,  -3.44040341e-17,
          2.45179334e-16,   9.28416998e-17,  -3.36366559e-02,
          2.54777681e-01,   8.86323840e-02,   6.71337077e-01,
          4.10013127e-17,   2.24797585e-15,  -8.11392284e-02,
         -6.14580732e-01,   1.36693496e-15,   1.51453765e-01,
          1.14717102e+00,  -1.63712562e-15,  -5.10577618e-16,
         -1.78059291e-16,  -1.87252131e-18,  -9.03030555e-03,
         -6.83991043e-02,  -1.95772693e-16,   6.24884575e-18,
         -2.41335755e-16,  -6.06640536e-02,   4.59492430e-01,
         -4.63316829e-17],
       [  5.80021438e-04,   1.38500884e-03,  -3.62735082e-02,
          1.14105742e-01,  -2.13318241e-01,  -5.78331483e-16,
         -5.18459415e-16,  -1.31877053e-15,  -1.66697999e-16,
         -2.63216008e+00,   9.45818968e-01,   1.40904871e-15,
          2.26194376e-15,   1.81424462e-01,  -2.52416855e-16,
         -1.59087874e-15,   1.89415011e-01,  -2.73530166e+00,
          1.32345157e-16,  -2.62985955e-09,   1.22051334e-15,
          7.87315798e-17,   3.58398917e-14,   2.30801463e-08,
         -5.50174240e-01,   2.70290318e-15,   5.42542677e-16,
          1.63203628e+00],
       [ -4.01282170e-04,  -1.20937464e-03,  -2.85380596e-02,
          1.34151027e-02,  -2.49804575e-02,  -4.80049413e-16,
         -1.69680125e-16,   1.10171117e-16,  -7.65923908e-17,
         -5.37891093e-02,  -7.14833576e-02,   1.20206691e-16,
         -1.86501725e-16,   6.36208587e-02,   3.72949126e-17,
         -1.00195504e-17,   2.30412288e-01,  -2.17093025e-01,
          1.67781562e-17,   1.26615006e-08,   2.42035821e-16,
         -4.98429363e-18,   8.66774717e-15,   5.59486856e-09,
         -8.35122694e-01,   3.71123605e-15,   1.29305403e-15,
          1.19988910e+00],
       [  1.29465921e-18,   1.92617306e-19,   1.59019527e-17,
          2.11575847e-16,   1.07020697e-16,   4.71221027e-02,
          6.22122706e-03,   1.28593379e-02,  -1.69773798e-03,
          6.33510031e-17,   7.28745384e-17,  -1.02533002e-01,
          1.35367858e-02,   2.33248613e-16,  -6.80532989e-02,
          8.98464903e-03,  -4.39264224e-16,   2.34655067e-17,
         -4.31821320e-16,  -4.62333092e-17,   5.90242762e-01,
         -7.79260451e-02,  -4.42840673e-17,  -1.39162868e-17,
          5.09795001e-15,   1.09386286e+00,   1.44416210e-01,
          2.88858660e-17],
       [ -3.46576401e-19,   1.69358554e-19,  -1.30677861e-18,
          1.78487874e-17,   5.52957928e-17,  -6.22123373e-03,
          4.71220522e-02,  -1.69773733e-03,  -1.28593428e-02,
         -1.77180782e-16,  -2.51178542e-16,   1.35367851e-02,
          1.02533007e-01,   1.40884927e-16,   8.98464783e-03,
          6.80533080e-02,  -4.87305532e-17,   8.71587857e-17,
         -1.17547700e-15,  -1.76251781e-17,  -7.79260447e-02,
         -5.90242765e-01,   1.58009495e-17,   2.36368494e-17,
          1.00951427e-15,  -1.44416210e-01,   1.09386286e+00,
          8.07324767e-18],
       [ -5.96923886e-10,  -4.30463314e-10,  -6.63748139e-09,
          8.15833822e-10,  -8.98878681e-09,  -5.20437644e-17,
         -1.41396786e-17,   3.69623731e-17,  -7.86567905e-17,
         -2.91988542e-09,  -1.28904791e-08,   4.34309797e-17,
         -2.06717367e-17,   2.86316738e-08,  -2.36680691e-17,
         -1.89984948e-17,  -8.52747912e-10,   7.89596089e-09,
          1.69491912e-01,  -6.30711159e-01,   5.05773472e-17,
         -2.31683555e-16,  -2.01703998e-01,   7.50583009e-01,
         -5.78180798e-09,  -1.09722678e-17,   8.68375677e-17,
         -2.04793353e-09],
       [  1.60412209e-10,   1.15679022e-10,   1.78369986e-09,
         -2.19240188e-10,   2.41556953e-09,  -1.00703353e-16,
         -1.14315859e-16,   1.37411707e-17,  -3.72259132e-16,
          7.84664979e-10,   3.46407688e-09,   1.34747295e-16,
         -9.07731413e-17,  -7.69423063e-09,   7.37401865e-18,
         -1.76038276e-17,   2.29160169e-10,  -2.12189285e-09,
          6.30711159e-01,   1.69491912e-01,   2.36090430e-16,
         -1.02212070e-15,  -7.50583009e-01,  -2.01703998e-01,
          1.55375352e-09,  -1.23251589e-17,   3.48465666e-16,
          5.50344096e-10],
       [ -7.07296715e-01,   7.08389687e-01,   8.64165974e-03,
          3.47517494e-03,  -1.14436900e-02,   1.64725992e-16,
          4.29333413e-17,   7.08115678e-17,   1.73275870e-17,
         -3.07566069e-02,  -1.57713606e-01,   3.63698234e-17,
         -6.87208891e-16,   4.27104890e-01,   1.50642536e-15,
         -1.18490922e-15,  -1.45125097e-01,  -6.47187332e-01,
          3.26939993e-17,   1.98058261e-08,   5.16116261e-17,
         -1.71433557e-16,   9.99335460e-15,   6.43455610e-09,
          3.87021589e-01,  -1.67896981e-15,  -5.89709746e-16,
         -1.80200661e-01],
       [ -3.82249923e-04,   1.66259928e-03,  -3.34086476e-01,
          3.27485529e-01,   9.61151106e-02,  -9.30419340e-16,
         -3.00923817e-16,   8.31880368e-19,  -1.10031011e-17,
          1.68727992e-01,  -3.01626331e-01,   4.64577956e-16,
         -1.44894825e-15,   1.03853186e+00,   3.62389604e-15,
         -2.77852430e-15,  -2.25810008e-01,  -1.43833996e+00,
          7.36574216e-17,   4.87802033e-08,   1.58188090e-16,
         -4.58382933e-16,   2.15317523e-14,   1.38618916e-08,
          7.28242309e-01,  -3.15097165e-15,  -1.06920647e-15,
         -4.81572779e-01],
       [  1.60307814e-03,  -4.59916822e-03,  -1.94141431e-01,
          4.21919705e-01,   3.30574419e-01,  -1.48773316e-15,
          2.42109260e-18,   1.22499604e-15,   1.76411810e-16,
          3.93920485e+00,   2.49674946e-03,   8.06909080e-16,
         -7.11826252e-17,  -9.33567630e-01,  -2.90414383e-15,
          4.66723011e-15,   6.43687511e-01,   6.09012017e+00,
         -3.01460053e-16,  -4.20834258e-08,  -1.50066205e-15,
          2.10615443e-16,  -8.88841398e-14,  -5.72541113e-08,
         -3.29154883e-01,   1.20886014e-15,   1.04731378e-15,
         -3.21852717e+00],
       [  4.46966781e-18,  -5.24698368e-18,   1.20529666e-17,
          1.60029006e-15,   2.90274206e-16,   4.22744597e-01,
          5.58122666e-02,   4.24107906e-01,  -5.59922808e-02,
         -7.08697537e-17,   8.66207092e-16,  -6.36852101e-01,
          8.40795869e-02,   3.53146361e-15,  -7.26344459e-01,
          9.58946849e-02,   4.11064509e-16,  -7.21010121e-17,
          2.73107158e-16,   5.50163463e-17,  -2.86842953e-01,
          3.78700707e-02,  -8.35617913e-17,   1.68477474e-17,
         -1.29760482e-15,  -2.40896783e-01,  -3.18041713e-02,
         -2.73482277e-17],
       [ -5.06845913e-19,   4.58825184e-19,  -1.63415873e-17,
          1.61235494e-16,   3.26172961e-16,  -5.58123003e-02,
          4.22744342e-01,  -5.59922936e-02,  -4.24107809e-01,
          6.60401553e-19,  -1.27966369e-15,   8.40795633e-02,
          6.36852280e-01,   1.94568708e-15,   9.58946779e-02,
          7.26344513e-01,  -4.88894721e-16,  -1.27498385e-16,
          4.75758777e-16,   8.70447597e-18,   3.78700735e-02,
          2.86842932e-01,  -3.53449583e-16,   6.30477942e-18,
         -2.59082466e-16,   3.18041700e-02,  -2.40896793e-01,
          2.65159542e-18],
       [  1.37260556e-03,  -2.36276482e-03,   2.17748589e-01,
          2.15878284e-01,   4.54265589e-01,  -1.24325457e-15,
         -6.59013240e-16,   3.07180699e-17,   1.78949358e-17,
         -6.05578251e-02,   4.60283493e-01,   1.14165472e-15,
          1.28126002e-15,   2.69004274e-01,   3.07807848e-16,
         -1.79516744e-15,  -7.55769681e-01,   1.28194696e-01,
          9.15834194e-19,  -2.60732912e-09,  -1.00511326e-16,
          1.47790220e-16,   3.64969597e-16,   2.46057423e-10,
         -3.66006395e-01,   1.46913928e-15,   5.52937840e-16,
          1.07198186e+00],
       [  8.07107812e-20,  -1.59168484e-19,   8.54559311e-18,
          9.49936952e-16,   2.72760260e-16,   2.54777432e-01,
          3.36366888e-02,   6.71336935e-01,  -8.86324028e-02,
         -5.08846873e-16,  -1.62021586e-16,   6.14580834e-01,
         -8.11392149e-02,  -4.58858432e-15,   1.14717110e+00,
         -1.51453754e-01,   5.11187281e-17,   1.10026841e-16,
          1.40345153e-16,  -1.47783489e-17,   6.83991150e-02,
         -9.03030415e-03,   1.30069120e-16,  -5.14997633e-18,
         -2.33500956e-15,  -4.59492430e-01,  -6.06640536e-02,
         -1.00853860e-17],
       [ -1.17461398e-19,   4.07673593e-19,  -6.20661036e-19,
          6.40698628e-17,   1.86707034e-16,  -3.36366559e-02,
          2.54777681e-01,  -8.86323840e-02,  -6.71337077e-01,
          1.97666050e-16,   9.68821089e-16,  -8.11392284e-02,
         -6.14580732e-01,  -2.65379550e-15,  -1.51453765e-01,
         -1.14717102e+00,   9.65268452e-16,   2.08175069e-16,
         -7.73276058e-18,   4.15189501e-18,  -9.03030555e-03,
         -6.83991043e-02,   1.92237700e-16,  -2.71521216e-18,
         -3.84864543e-16,   6.06640536e-02,  -4.59492430e-01,
          2.18878868e-18],
       [ -5.80021438e-04,   1.38500884e-03,   3.62735082e-02,
          1.14105742e-01,   2.13318241e-01,  -6.07780024e-16,
         -4.76130281e-16,  -5.95989634e-16,   2.32130398e-17,
         -2.63216008e+00,  -9.45818968e-01,  -3.35846419e-15,
         -1.93258398e-15,  -1.81424462e-01,   7.52700507e-17,
          3.08422211e-16,   1.89415011e-01,  -2.73530166e+00,
          1.27054881e-16,   2.62985762e-09,   8.09771686e-16,
          1.46920988e-16,   3.58368943e-14,   2.30801463e-08,
          5.50174240e-01,  -2.31232350e-15,  -1.26681027e-15,
          1.63203628e+00],
       [ -4.01282170e-04,   1.20937464e-03,  -2.85380596e-02,
         -1.34151027e-02,  -2.49804575e-02,  -1.07994889e-16,
         -2.31587276e-16,  -2.10776864e-16,  -3.74628305e-17,
          5.37891093e-02,  -7.14833576e-02,  -1.10192274e-16,
          4.75863559e-17,   6.36208587e-02,   2.99437846e-16,
         -4.44342404e-16,  -2.30412288e-01,   2.17093025e-01,
         -6.99433877e-18,   1.26615008e-08,  -1.45129904e-16,
          1.39376676e-16,  -8.65886364e-15,  -5.59486871e-09,
         -8.35122694e-01,   3.74466902e-15,   1.32773178e-15,
         -1.19988910e+00],
       [ -8.85232879e-19,   1.57741515e-18,  -1.29639192e-17,
         -1.37228526e-16,   5.49719107e-17,  -4.71221027e-02,
         -6.22122706e-03,   1.28593379e-02,  -1.69773798e-03,
         -7.28319239e-17,  -1.50002016e-16,   1.02533002e-01,
         -1.35367858e-02,   8.20171433e-17,  -6.80532989e-02,
          8.98464903e-03,   5.41826548e-17,  -9.62018038e-17,
          1.88453299e-16,   5.07758602e-17,  -5.90242762e-01,
          7.79260451e-02,  -2.57506728e-18,   3.59953261e-17,
          5.09432415e-15,   1.09386286e+00,   1.44416210e-01,
          6.17421730e-17],
       [  2.69099407e-19,   7.68087575e-20,   4.29405414e-18,
         -7.04489744e-18,  -1.95725464e-17,   6.22123373e-03,
         -4.71220522e-02,  -1.69773733e-03,  -1.28593428e-02,
          1.18909845e-16,   3.03471766e-16,  -1.35367851e-02,
         -1.02533007e-01,   3.17106047e-17,   8.98464783e-03,
          6.80533080e-02,  -8.71593254e-17,  -1.60768970e-16,
          6.38597817e-16,   1.23848541e-17,   7.79260447e-02,
          5.90242765e-01,   1.58353102e-16,  -8.36749328e-18,
          1.10641006e-15,  -1.44416210e-01,   1.09386286e+00,
         -1.82488500e-18],
       [ -5.96923884e-10,   4.30463312e-10,  -6.63748137e-09,
         -8.15834043e-10,  -8.98878683e-09,  -1.67648950e-17,
          8.12308965e-18,  -1.58737838e-17,   4.72438825e-17,
          2.91988538e-09,  -1.28904791e-08,   1.35995137e-17,
         -1.08752342e-17,   2.86316737e-08,  -1.03451744e-17,
         -5.11222287e-19,   8.52747930e-10,  -7.89596040e-09,
          1.69491912e-01,  -6.30711159e-01,  -2.96891761e-17,
         -2.95654540e-16,   2.01703998e-01,  -7.50583009e-01,
         -5.78180784e-09,   2.65547184e-17,   2.66986797e-17,
          2.04793353e-09],
       [  1.60412209e-10,  -1.15679021e-10,   1.78369986e-09,
          2.19240248e-10,   2.41556954e-09,  -9.49008646e-17,
         -1.26228867e-17,  -1.23338011e-16,   2.18060238e-16,
         -7.84664974e-10,   3.46407688e-09,   8.03218568e-17,
         -4.86516844e-17,  -7.69423063e-09,   3.85551583e-18,
         -2.70565865e-17,  -2.29160170e-10,   2.12189279e-09,
          6.30711159e-01,   1.69491912e-01,   2.27213299e-16,
         -1.13184937e-15,   7.50583009e-01,   2.01703998e-01,
          1.55375350e-09,   6.92535367e-17,   8.25201113e-17,
         -5.50344097e-10]])

    results = ['ref_result_energy', 'ref_result_exp_alpha']
    thresholds = {'ref_result_exp_alpha': 1e-08, 'ref_result_energy': 1e-08}

    test_path = context.get_fn("examples/hf_dft/rhf_n2_dense.py")
    with open(test_path) as fh:
        exec fh

    l = locals()
    for r in results:
        var_name = r.split("ref_")[-1]
        assert allclose(l[var_name], l[r], thresholds[r]), l[r] - l[var_name]