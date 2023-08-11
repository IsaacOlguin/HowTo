import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp(" ".join(['AS TO THE LAW', '1. Matznetter ’ s Application raised, in the parts which the Commission has declared admissible, two points which the Court has to determine. The first point concerns the duration of the detention of the Applicant while on remand (Article 5 (3) of the Convention) (art. 5-3); the second point relates to the conditions in which his various applications for release were decided (Articles 5 (4) and 6 (1)) (art. 5-4, art. 6-1).', 'A. As to the question whether the detention of Matznetter while on remand exceeded the reasonable time laid down in Article 5 (3) (art. 5-3) of the Convention', '2. Under Article 5 (3) (art. 5-3), "everyone arrested or detained in accordance with the provisions of paragraph (1) (c)" of that Article (art. 5-1-c) "shall be entitled", inter alia, "to trial within a reasonable time or to release pending trial" and such "release may be conditioned by guarantees to appear for trial".', '3. In its judgment of 27 June 1968, in the Neumeister case (page 37, paragraph 5), the Court held that "it is essentially on the basis of the reasons given in the decisions on the applications for release pending trial, and of the true facts ( ‘ faits non controuvés ’ ) mentioned by the Applicant in his appeals, that the Court is called upon to decide whether or not there has been a violation of the Convention". The Court also expressed the same view in the judgment it delivered on the same date in the Wemhoff case (page 24, paragraph 12).', 'The Court does not find to be well-founded the objections which the Austrian Government has made in this case to that method. On this point the Court refers to its judgment in the Stögmüller case (As to the Law, paragraphs 3 and 4).', '4. The Austrian Government has also disputed the extent of the period of detention to which the Commission ’ s examination was directed, that is, from the arrest of Matznetter ( 15 May 1963 ) to his release ( 8 July 1965 ). In the view of the Austrian Government, that period should not extend beyond the lodging of the application ( 3 April 1964 ) or even beyond the last final national decision given on a request for release which preceded the lodging ( 4 March 1964 ).', '5. The Court has already had occasion to pronounce itself on the question whether or not it could take account of facts which were subsequent to the application but were directly related to the facts covered by the application, and it answered this question in the affirmative. In its judgment of 1 July 1961 in the Lawless case (page 51, paragraph 12), the Court took into account the Applicant ’ s internment from 13 July to 11 December 1957 even thought the lodging of the Application dated from 8 November 1957. Similarly, in the Neumeister case the Court examined the entire period of the detention of Neumeister from 12 July 1962 to 16 September 1964, the date on which he recovered his freedom, that is, more than one year after he had petitioned the Commission (12 July 1963).', 'The Court refers to the reasons stated in this last-mentioned judgment (page 38, paragraph 7). The Court finds, moreover, that it is in accordance with national and international practice that a court should hold itself competent to examine facts which occurred during the proceedings and constitute a mere extension of the facts complained of at the outset. This is clearly the case in matters of detention while on remand, as courts seized of an application for release take their decisions in the light of the situation which exists at that time. For their part, international judicial bodies have frequently held that compensation for damage resulting from an illegal act of a state must also cover damage suffered by the applicant party after the institution of international proceedings.', '6. In the present case, the Austrian Government has, however, put forward in support of its case a line of argument grounded on Article 26 (art. 26) of the Convention. While acknowledging the interest of these arguments, the Court notes that they were not submitted to the Commission: quite the contrary, the Government did not cease to participate in the examination, before the Commission, of the period of Matznetter ’ s detention right up to his release (see Appendices II and III to the report of the Commission and the note of the hearing held on 5 July 1965, passim). The Court has not felt justified, however, in refusing to examine the new submissions which the Government has made on the basis of Article 26 (art. 26) but it can accept them to the extent indicated in its judgment given this day in the Stögmüller case (As to the Law, paragraphs 9 to 12).', '7. One finds in this case that when the application was lodged with the European Commission on 3 April 1964, a first request for release made on 27 December 1963 by the Applicant to the Austrian judicial authorities had been rejected at final instance on 4 March 1964.', 'The Court of Appeal of Vienna based its decision on the existence on the one hand of a danger of absconding and on the other hand on a danger of repetition of offences. As these two factors are not irrelevant to the scope of Article 5 (3) (art. 5-3) of the Convention, the Court finds itself called upon to ascertain whether they justified, in this case, the continuation of the detention.', '8. As regards the danger of absconding, the decisions refusing the request for release of 27 December 1963 contained extensive statements of reasons and were justified at that time. In particular, the circumstances of the arrest, the transfers of funds out of Austria, Matznetter ’ s journey to Angola and the connections which he had established abroad could, at the beginning, bear out the idea of such a danger.', '9. As to the danger of repetition of the offences, which may suffice under Austrian law to justify the continued remand in custody of a person charged or accused, the Court is prepared to hold such a reason to be compatible with Article 5 (3) (art. 5-3) of the Convention in the special circumstances of the case. A judge may reasonably take into account the seriousness of the consequences of criminal offences when there is a question of taking into account the danger of seeing such offences being repeated, in order to decide if the person concerned can be released in spite of the possible existence of such danger. In this case the Austrian courts took care to point in their decisions to a series of definite factors and the Court finds it proper that they should have attached importance to them, i.e. the very prolonged continuation of reprehensible activities, the huge extent of the loss sustained by the victims and the wickedness of the person charged.', 'The Applicant certainly maintained for his part that the" Schiwitz enterprises", thenceforth being managed by the Creditanstalt-Bankverein, were in course of liquidation and his own private office had been put under the control of a temporary administrator; he added that he was doing his utmost to assist in the finding out of the truth after having participated in the negotiation of a settlement out of court between the" Schiwitz enterprises" and their creditors. In the Court ’ s view, these explanations nonetheless lack weight when measured against the various circumstances mentioned by the Austrian courts, particularly the Applicant ’ s experience and great skill which were such as to make it easy for him to resume his unlawful activities either on his own account or in the employ of persons other than the" Schiwitz enterprises".', '10. As the Court has reached the conclusion that at the date of the lodging of the application Matznetter ’ s detention while on remand had not exceeded a reasonable time, it is led to ascertain, before examining the later detention, whether the continuation of this detention was not due to the fact that the Applicant had failed to make further requests to the Austrian judicial authorities.', 'The Court finds in this case that after the first request had been dismissed on 4 March 1964, Matznetter made, on 13 November 1964, a second request which was rejected in final instance on 20 January 1965 by the Court of Appeal of Vienna and then a third on 21 April 1965 which led to his release on 8 July 1965.', 'In the opinion of the Court, the time which elapsed between the final dismissal of the first request and the making of the second was not abnormal; the same holds good for the period between the final dismissal of the second request and the filing of the third. It must therefore be accepted that, at that time, the rule of exhaustion of domestic remedies was observed. The Court therefore finds itself justified in directing its examination, as did the Commission, to the period of detention extending right up to the Applicant ’ s release.', '11. The reasons given by the Austrian courts for the dismissal of the second request for release are the same as those on which they had relied to dismiss the first request.', 'As regards the danger of absconding, however, in his second application for release (13 November 1964) and in his appeals and supporting documents, the Applicant gave, on the circumstances of fact which the Austrian courts took into account, explanations which were not refuted and which the Court considers normal and credible. The applicant stressed, for example, that he himself had revealed to the investigating authorities the transfer of funds at issue and that at the time of his arrest he was not carrying his passport on his person as he had left it in town in his damaged motor car. As regards the severity of the sentence to be expected, on which the Austrian authorities based a further reason, it cannot suffice, in the Court ’ s view, to establish the existence of a danger of absconding; in any event, the effect of the fear which such severity inspires in a person charged or accused diminishes as the detention continues and, consequently, the balance of the sentence which the person concerned may expect to have to serve is reduced (judgment of 27 June 1968 in the Wemhoff case, page 25, paragraph 14; judgment of 27 June 1968 in the Neumeister case, page 39, paragraph 10). In any case, the national authorities would have been able to accept the security offered by the Applicant if the sole reason for his detention had been the danger of absconding.', 'The Court considers that if the danger of absconding could no longer be found to be sufficient in this case, on the contrary and for the reasons set out above, the danger of repetition of offences could be held to justify the continuation of the Applicant ’ s detention while on remand.', 'In its decision of 8 July 1965, the Judges ’ Chamber acknowledged that, having regard to Matznetter ’ s serious illness, this danger had ceased to exist. In the Court ’ s opinion the Austrian courts could scarcely have arrived earlier at this last conclusion. The Applicant had admittedly made known his state of health as early as 7 January 1964 but without relying much on the point and then, it seems, for the sole purpose of showing that there was no danger of his absconding: besides, he had never been admitted to the prison hospital before he made his application of 21 April 1965.', '12. It remains to see whether in this case the Austrian judicial authorities displayed the special diligence which the Convention requires in the case of a detained person. Some delays may in effect constitute violations of Article 5 (3) (art. 5-3) while remaining compatible with Article 6 (1) (art. 6-1); as the Court has observed in its judgment in the Stögmüller case (As to the Law, paragraph 5), the two provisions are not identical with one another.', 'The Court does not find, however, that the length of Matznetter ’ s detention, from 15 May 1963 to 8 July 1965, was due to the slowness of the preliminary investigation which ended only on 11 May 1965; the Court shares the Commission ’ s opinion that no criticism can be made of the judicial authorities ’ conduct of the case. The unusual length of the investigation is justified by the exceptional complexity of the case. It is true that intervals of several months elapsed between different interrogations of Matznetter (from 20 May to 20 November 1963 and from 7 February to 27 August 1964); moreover, Matznetter was scarcely heard before 27 August 1964 - that is, more, than fifteen months after his arrest - on the part he himself had taken in the alleged dishonest operations. However, the Court finds that the explanations given on this point by the Investigating Judge and the Government are credible (see above the section "arguments of the Commission and of the Government", paragraph 5, and report of the Commission, paragraph 20, paragraph 71 and Appendix IV). The Court further observes that the competent authorities ordered certain charges to be split up and relieved the Investigating Judge, from 20 November 1963 to 10 May 1965, from his duty to take on new cases, thus showing their anxiety to avoid any delay in the course of the proceedings (report of the Commission, paragraphs 72-73 and Appendix IV). Besides, it should not be overlooked that, while an accused person held in custody is entitled to have his case given priority and conducted with special diligence this must not stand in the way of the proper administration of justice; the Court refers, on this point, to its judgment in the Wemhoff case (pages 25-26, paragraphs 16 and 17).', 'B. As to the question whether or not the procedure followed in the examination of Matznetter ’ s applications for release gave rise, by reason of a lack of "equality of arms", to a violation of Article 5 (4) or Article 6 (1) (art. 5-4, art. 6-1), or possibly of these two provisions read together', '13. A similar issue already arose before the Court in the Neumeister case : the Court ’ s judgment of 27 June 1968 (pages 43-44, paragraphs 22 to 25) decided the point in the negative. The Court sees no reason to depart in this case from that decision, with which, incidentally, the Commission and the Government have indicated their agreement at the public hearings.']))


for token in doc:
    if token.ent_type:
        print(token, token.ent_type_)
    #else:
    #    print(token, "###")