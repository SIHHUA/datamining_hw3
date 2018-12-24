clear all
for i=1:6
    data{i}=load(['graph_' int2str(i) '.txt']);
end

for i=1:5
    node=max(max(data{1,i}));
    connect_ar=spalloc(node,node,length(data{1,i}));
    for j=1:length(data{i})
        connect_ar(data{1,i}(j,1),data{1,i}(j,2))=1;
    end
        simrank{i}=SimRank(connect_ar,node,0.01,50,0.3);
end

%% SimRank
function result=SimRank(connect_ar,node,delta,iter,C)
S=zeros(node,node);
S_o=S;
time=1;
for i=1:node
    L{i}=find(connect_ar(:,i));
end
while(time<iter)
    for i=1:node
        for j=i:node
            if(i==j)
                S(i,j)=1;
            elseif isempty(L{i})
                S(i,j)=0;
                break;
            elseif isempty(L{j})
                S(i,j)=0;
            else
                S(i,j)=C/length(L{i})/length(L{j});
                tmp=0;
                for i2=1:length(L{i})
                    for j2=1:length(L{j})
                        tmp=tmp+S(L{i}(i2),L{j}(j2));
                    end
                end
                S(i,j)=S(i,j)*tmp;
                S(j,i)=S(i,j);
            end
        end
    end
        if norm(S_o-S)<=delta
            break;
        end
    S_o=S;
    
    time=time+1;
end
result=[S,(1:node)'];
end








